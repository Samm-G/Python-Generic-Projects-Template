# Python Generic Projects Template

Create all required file for the template:
```bash
python template.py
```

Create a Conda Env to start development:
```bash
bash init_setup.py -v 3.7.12
```

Test your project:
```bash
# Run tests
tox

# Run with recreation of all envs again, (If requirements.txt changes)
tox --recreate
```

See Docs for you project:
```bash
mkdocs serve
```

TODO: Steps to configure for my project:
1) Include:
   1) Create Separate Project Package? (setuptools package)
   2) Need Conda Env? (init_bash.sh)
   3) Github Workflows required?
   4) Tests?:
      1) Tox? (tox)
         1) Local Tests?
         2) Github Tests?
      2) Pytests? (pytest -v)
   5) DVC required?
      1) Research Notebook to Stages Decomposition functionality?
   6) Logger required?
   7) Requirements templates to generate:
      1) Separate Dev and Prod Requirements.txt ? (requirements_dev.txt and requirements.txt)
      2) DL generic?
      3) ML generic?
      4) etc..
   8) Need Docs?
      1) MKDocs?
      2) Sphinx?
      3) Need to include API references?
   
2) Different Workflows:
   1) Create Env (init_bash.sh)
   2) DVC Repro
   3) Run tests (tox)


3) Later:
   1) Integrate these into an Aasare Template.
   2) Fork this into a .aasr template:
      1) This templater will contain 
         1) aasare.py (command: aasare.py unpack)
         2) template.aasr

Thanks to:
- Sunny Bhaveen Chandra: <https://github.com/c17hawke>