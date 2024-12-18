class BjedBjed:

    def __init__(self):
        self.username = 'bjedbjed'
        self.name = 'Blazej'
        self.definition = 'self motivated learner'
        self.background = 'Financial Engineer' 
        self.now = 'Data Analyst'
        self.country = 'Poland'
        self.languages = {
            'polish': 'Native',
            'english': 'Advanced',
            'chinese': 'Intermediate',
        }
        self.skills = {
            'technical': ['Python', 'SQL', 'Postgres SQL','My SQL', 'Pandas', 'Numpy', 'PyTorch', 'Matplotlib.pyplot', 'Seaborn',
                          'Plotly', 'Scikit-learn', 'Jupyter Notebook', 'Visual Studio Code', 'Visual Basic', 'Algorithms',]
        }

    def __str__(self):
        return self.name

if __name__ == '__main__':
    me = BjedBjed()
