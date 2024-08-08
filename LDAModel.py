import mne
import mne_bids
from mne    import Epochs
from mne.io import Raw
import pandas as pd
import numpy as np
import os
import sys
from loguru import logger

from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, cross_val_score


# cutom import
import my_utils as util

class MyLDA():
    def __init__(self):
        pass

    def decode_binary(self, X, y, meta, times= None, to_print_csv = False):
        """
        y is expected to be binary with value True or False
        """
        logger.info("decod_binary is running")
        try:
            assert len(X) == len(y) == len(meta)
        except AssertionError:
            logger.error(f"X, y meta is not of same length, len(X)={len(X)}, len(y)={len(y)}, len(meta)={len(meta)}")
            return None
        logger.debug(f"in decod, len(x)=len(y)=len(meta)={len(X)}")
        logger.debug(f"X.shape: {X.shape}")
        logger.debug(f"y.shape: {y.shape}")
        logger.debug(f"meta.shape: {meta.shape}")
        meta = meta.reset_index()

        # Initialize the scaler and the LDA model
        scaler = StandardScaler()
        lda = LinearDiscriminantAnalysis()

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        scores = []
        y_train = np.array(y_train, dtype=bool)     # convert y to format lda model expect
        # which needs to be np arr with dtype numeric or bool
        
        n, nchans, ntimes = X.shape
        preds = np.zeros((len(X_test), ntimes, 2))  # Adjusted to store probabilities for both classes
        pred = None # tmp pred for one time point
        df = None # tmp df for one time point

        # predict by my self
        for t in range(1):
            # Scale the data
            # X_train_scaled = scaler.fit_transform(X_train[:, :, t])
            # X_test_scaled = scaler.transform(X_test[:, :, t])

            # Fit the LDA model
            print("X_train[:, :, t]:", X_train[:, :, t].shape)
            print("y_train:", y_train.shape)
            lda.fit(X_train[:, :, t], y_train)
            logger.info(f'n_components: {lda.n_components}')


            # Predict probabilities by projected X form the fitted LD
            pred = lda.predict(X_test[:, :, t])

            # add code to make a df of preds
            df = pd.DataFrame(pred, columns=["pred"])
            
        
        # below still need debug
            
        # evaluate by k fold
        # for t in range(1):
        #     cv = RepeatedStratifiedKFold(n_splits=5, n_repeats = 3, random_state=1)
        #     # n_split = no. of folds
        #     score = cross_val_score(lda, X, y, scoring="accuracy", cv=cv, n_jobs=-1)
        #     scores.append(score)


        return df, None
        return df, scores