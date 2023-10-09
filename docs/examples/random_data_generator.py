import numpy as np

"""
Quick script to generate random data for examples

In this example:
    volume = grain volume
    dms = delta max schmid, or the largest difference between max schmid factors in a grain
    num_neighbors = number of neighbors that a grain has
    nst = number of active slip systems in the grain
    t_factor = the taylor factor of a grain
    e_one = the first principal strain component of a grain
    sin_nst = the sin of the nst with a multiplying factor 
    num_elem = the number of elements in the slip band where the FIP is located.
    fip = fatigue indicator parameter. In this case the grain averaged FIP.

Rip this code and generate your own random data if that would help. 

NOTE: This is dummy data intended to show the functionality of PolyFlow.
      Do not use for legitimate model development.

"""

def main():
    #
    # Define features and their range
    #
    features = {'volume':(4000,200000),
                'dms': (-0.2, 0.2),
                'num_neighbors': (1,6),
                'nst': (0,8),
                't_factor': (40,2300),
                'e_one': (0.0042,0.012),
                'sin_nst': (-1,1),
                'num_elems': (10,128)}

    #
    # Generate random data within feature ranges
    #
    # First feature
    print('Generating dummy data...')
    num_samples = 4000
    init_bound = list(features.values())[0]
    dummy_data = np.random.uniform(init_bound[0], 
                 init_bound[1], size=(num_samples,1))
    
    # All other features
    for bounds in list(features.values())[1:]:
        # stack remaining features
        dummy_data = np.hstack(
                        (dummy_data, np.random.uniform(bounds[0], 
                         bounds[1], size=(num_samples,1))))
    
    # Write
    print('Saving dummy data...')
    # txt
    np.savetxt('dummy_data.txt', dummy_data, delimiter=' ')
    #with open('dummy_data.txt', 'w') as f:
    #    for line in dummy_data:
    #        f.write(f'{line}\n')
    # npy
    np.save('dummy_data.npy', dummy_data)
    # csv
    np.savetxt('dummy_data.csv', dummy_data, delimiter=',')

if __name__ == '__main__':
    main()





