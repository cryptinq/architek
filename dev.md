### Boot sequence :

* [OK] Load the kernel
* [OK] Load the configurations files

* [OK] Initialize the core providers
  * [OK] Load the environment variables provider
 
* Initialize the core services
  * Initialize the logger
  * Initialize the arguments parser
  * Initialize the database connection
  
* Initialize the ORM (= entities & repositories)

* Initialize the services

* Load user app

### Console :

Run `python console`

- `database` : database commands
  - `create` : create the database
  - `drop` : drop the database
  - `recreate --seed` : drop & create the database
  - `seed` : seed the database


- `entities` : entities commands
  - `generate [--force]` : generate the entities