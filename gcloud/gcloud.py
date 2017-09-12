# Make parent module available for import
import sys 
sys.path.append('..')

import provider

class GCloud(provider.Provider):
    class storage(provider.Provider.storage):
        def cp(self, args):
            print('FAKE gcloud cp', args)
        def rm(self, args):
            print('FAKE gcloud rm', args)
