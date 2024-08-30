# fishmlserv

### Deploy
![image](https://github.com/user-attachments/assets/5ba77e0a-1989-4a6a-b518-85373e628064)


### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.finshmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```
