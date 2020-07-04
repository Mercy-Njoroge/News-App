class News_source:
    '''
    Class for instantiating Source objects
    '''
    def __init__(self,name,description,category,url,id):
        '''
        Method for instantiating the movie variables
        '''
        self.name = name
        self.description = description
        self.category =category
        self.url = url
        self.id = id