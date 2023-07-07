from feat import Feat
import numpy as np
from sklearn.preprocessing import *

def main():
    
    parser = argparser.ArgumentParser()
    parser.add_argument('--store_path', required=True)
    parser.add_argument('--feat_config_path' requred=True)
    parser.add_argument('--feat_seed_metadata', default={})

    store_path = args.store_path
    feat_config_path = args.feat_config_path
    feat_seed_metadata = args.feat_seed_metadata

    #
    # Import data from Kosh using appropriate preprocessing steps
    #     
    micro_df = pd.read_csv('train_80.csv',header=0) #research

    micro_df_test = pd.read_csv('test_80.csv',header=0)
    X_test = micro_df_test.drop(columns=['FIP']).to_numpy(dtype=float)
    y_test = micro_df_test['FIP'].to_numpy(dtype=float)

    X = micro_df.drop(columns=['FIP']).to_numpy(dtype=float)
    y = micro_df['FIP'].to_numpy(dtype=float)

    #
    # FEAT setup
    # 
    # 1) Parse the feat config yaml

    # 2) Build feat object
    random_state = 42

    fest = Feat(pop_size=300, # population size
		gens=300, # maximum generations
		max_time=400, # max time in seconds
		max_depth=3, # constrain features depth
		max_dim=5, # constrain representation dimensionality
		random_state=random_state,
		hillclimb=True, # use stochastic hillclimbing to optimize weights
		scorer = 'mse',
		iters=100, # iterations of hillclimbing
		n_jobs=1, # restricts to single thread
		functions = '+,-,/,*,exp,log,sqrt',
		verbosity= 1, # verbose output,
		otype='f',
		normalize=False
	       )

    #
    # Train FEAT
    #
    y = np.ravel(y)
    y_test = np.ravel(y_test)
    fest.fit(X,y)
    print(fest.get_model(sort=False))
    y_pred = pd.DataFrame(fest.predict(X_test))
    #y_pred['Element'] = micro_df.index
    print('equation: ', fest.get_eqn())
    print('MSE: ', fest.score(X_test,y_test))
    #y_pred.to_csv('FEAT_pred_B_ex.csv',index=False)

    #
    # Save feat terms as seeds (str) to Kosh for later use in Bingo
    #

