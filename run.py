#!/home/creed347/anaconda3/envs/fastAPI/bin/python
import uvicorn


def main():
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8080,
        reload=True,
    )


if __name__ == "__main__":
    main()
