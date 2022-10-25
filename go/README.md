<img src="./preview.png" />

```bash
# steps to run

go mod download
go mod verify

rm -rf bin

cd client && go build -o ../bin/go-client && cd ../
cd server && go build -o ../bin/go-server && cd ../
```
