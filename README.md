class bjedbjed:

    def __init__(self):
        self.username = 'bjedbjed'
        self.name = 'Blazej'
        self.definition = 'Self motivated learner'
        self.background = 'Financial Engeener' 
        self.now = 'Data Science Student'
        self.country = 'Poland'
        self.polish = 'Native'
        self.english = 'Advanced'
	self.chinese = 'Intermediate'
        self.skills = {
          'technical':['Python','SQL', 'SQL Server', 'Pandas', 'Numpy','PyTorch', 'Matplotlib.pyplot', 'Sklearn', 'Jupyter Notebook'. 'Visual Studio Code','Algorithms']
        }

    def __str__(self):
        return self.name

if __name__ == '__main__':
    me = bjedbjed()
