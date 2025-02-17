import polars as pl
def main():
    print("Hello, World!")
    df = pl.read_csv("data/iris.csv")
    a = 1

if __name__ == "__main__":
    main()