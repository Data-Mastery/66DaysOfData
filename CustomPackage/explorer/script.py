import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.data = None
        self.title = "Default"

    def load_data(self, path):
        '''
        Parameters
        ----------
        path : TYPE
            Path on your local folder with a .csv file

        Returns
        -------
        None.

        '''
        self.data = pd.read_csv(path)

    def visualize(self, grid=False):
        '''
        Parameters
        ----------
        grid : TYPE, optional
            Boolean value if plots are generated in a grid or in a loop. Default is False

        Raises
        ------
        ValueError
            DESCRIPTION.

        Returns
        -------
        None

        '''
        if self.data is None:
            raise ValueError("You have to provide a dataframe first. Please run the load_data() with a dataframe")
        
        if grid:
            fig, axes = plt.subplots(ncols=1, nrows=5)
            for i, ax in zip(range(len(self.data.columns)), axes.flat):
                sns.histplot(self.data, x=self.data.columns[i], ax=ax)
            plt.figure(figsize=(10, 8))
            plt.show()
        else:
            for i, col in enumerate(self.data.columns):
                plt.figure(i)
                sns.histplot(self.data, x=col)
            
    
