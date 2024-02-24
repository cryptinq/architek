### Boot sequence :

* [OK] Load the kernel

##### Core modules
* [OK] Load the configurations files
* [OK] Load the console
* [OK] Load the environment variables

##### Core services
* Initialize the logger (see later how to implement)

##### Core databases modules
* [OK] Initialize the database connection
* Initialize the ORM (= entities & repositories)

##### Application services
* Initialize the services

### Console :

Run `python console`

- `database` : database commands
  - `create` : create the database [OK]
  - `drop` : drop the database [OK]
  - `recreate [--seed]` : drop & create the database
  - `seed` : seed the database


- `entities` : entities commands
  - `generate [--force]` : (re) generate the entities