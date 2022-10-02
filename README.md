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
tox
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
   6) Requirements templates to generate:
      1) Separate Dev and Prod Requirements.txt ? (requirements_dev.txt and requirements.txt)
      2) DL generic?
      3) ML generic?
      4) etc..
   
   
2) Different Workflows:
   1) Create Env (init_bash.sh)
   2) DVC Repro
   3) Run tests (tox)


Thanks to:
- Sunny Bhaveen Chandra: <https://github.com/c17hawke>