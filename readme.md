Architek
---

**Architek** is a fully featured modern python cli apps developpment framework.  

Read the full [documentation](https://www.example.com)

**Installation :**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/cryptinq/architek/dev/bin/remote/install.sh)"
```

**Running the app**

Use `python console start` to boot up app/App.py  

### Entities

Create a file `database/schema/example.yaml` to define your schema :

``` yaml
entity:

  name: Example
  table: example
  timestamp: true
  key: { name: id, generator: autoincrement } # or { name: uuid, generator: uuid } or { name: my_row, generator: custom }
  fields:
    - id: { type: integer, primary: true, autoincrement: true }
    - name: { type: string, length: 255 }
```

Then run `python console schema:update` to create database and generate entity and repositories

Once done can access your repository using `self.repository(Example)` inside App or any class that inherit from Base

``` python
class App(Base):

    def __init__(self):
        super().__init__()
        self.example_repository: ExampleRepository = self.repository(Example)

    def boot(self):
        example: Example = Example(name="example")
        success = self.example_repository.save(example)
```

### Services

Go to `config/app/services.yaml` and define your service :
``` yaml
services:

  ExampleService: { namespace: app.services, identifier: app.example, singleton: true }
```

Then you can access your service using `self.service("your_identifier")` inside App or any class that inherit from Base

``` python
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

`python console help` : Get list of commands  
`python console start` : Start application  
`python console test` : Run tests

`python console cache:clear` : Clear application cache

`python console cache:clear` : Clear application cache

`python console entity:generate` : Generate entity & repositories from database scheme

`python console key:show` : Show application key  
`python console key:generate` : Generate application key

`python console make:command` : Create a new Command Class  
`python console make:service` : Create a new Service Class

`python console schema:update` : Create database, generate entities & repositories, seed database