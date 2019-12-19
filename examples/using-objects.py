# Simple example of creating 3 Kubernetes namespaces

# Our users in need of namespaces
# users = ['jim', 'sally', 'sue']

class Storage:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  skus = ['StandardLRS', 'StandardGRS']
  
  def getName(self):
    return "ol' man " + self.name

p1 = Storage("John", 36) # can easily work with python objects
p2 = Storage("Alex", 12)

people = [p1, p2] 

# The namespaces objects from YAML
storageAccounts = map(lambda account: <
        apiVersion: "2019-08-01"
        kind: !~ Storage.skus[1]
        metadata:
          name: !~ account.getName() # easy inline operations
          age: !~ account.age + 5
    >, people)

render(storageAccounts)