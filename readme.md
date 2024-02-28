### Installation

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cryptinq/architek/dev/bin/remote/install.sh)"
```

### Running the app

Use `python console start` to boot up app/App.py  

### Entities

todo

### Services

##### Registering a service

Go to `config/app/services.yaml` and define your service :
```
services:

  ExampleService: { namespace: app.services, identifier: app.example, singleton: true }

```

Then you can access your service using `self.service("your_identifier")` inside App or any class that inherit from Base

```
class App(Base):

    def __init__(self):
        super().__init__()
        self.example_service: ExampleService = self.service("app.example")

    def boot(self):
        self.example_service.example_method()
```

### Configuration

`config/app.yaml` : General application configuration  
`config/app/commands.yaml` : Define commands and arguments  
`config/app/database.yaml` : Configure database driver  
`config/app/logs.yaml` : Configure logging  
`config/app/services.yaml` : Define application services  

`database/schema/%schema%.yaml` : Define your database schemas

### Commands

##### Application

`python console help` : Get list of commands  
`python console start` : Start application  
`python console test` : Run tests

##### Cache

`python console cache:clear` : Clear application cache

##### Database

`python console cache:clear` : Clear application cache

##### Entity

`python console entity:generate` : Generate entity & repositories from database scheme

##### Key

`python console key:show` : Show application key  
`python console key:generate` : Generate application key

##### Make

`python console make:command` : Create a new Command Class  
`python console make:service` : Create a new Service Class

##### Schema

`python console schema:update` : Create database, generate entities & repositories, seed database