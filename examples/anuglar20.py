from angular2.angular2 import Component, View, bootstrap 
	


@Component({'selector': 'my-app'})
@View({'template': '<h1>Hello {{ name }}</h1>'})
class MyAppComponent():
    def __init__(self):
        self.name = 'Ahmed'
    def extrameth(self, param1):
        self.name = param1

