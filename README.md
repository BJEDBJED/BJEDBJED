class BjedBjed:

    def __init__(self):
        self.username = 'bjedbjed'
        self.name = 'Blazej'
        self.definition = 'Self motivated learner'
        self.background = 'Financial Engineer' 
        self.now = 'Data Science Student'
        self.country = 'Poland'
        self.languages = {
            'polish': 'Native',
            'english': 'Advanced',
            'chinese': 'Intermediate'
        }
        self.skills = {
            'technical': ['Python', 'SQL', 'SQL Server', 'Pandas', 'Numpy', 'PyTorch', 'Matplotlib.pyplot',
                          'Scikit-learn', 'Jupyter Notebook', 'Visual Studio Code', 'Algorithms']
        }

    def __str__(self):
        return self.name

if __name__ == '__main__':
    me = BjedBjed()
