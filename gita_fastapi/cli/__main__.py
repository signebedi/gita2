import click
from gita_fastapi.utils.chromadb_search import add_data, query_collection


@click.group()
def cli():
    """CLI for interacting with ChromaDB utilities."""
    pass


@cli.command()
@click.option(
    "--file-path", 
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    default=None,
    help="Path to the JSON file containing the data. If not provided, sample data will be used."
)
@click.option(
    "--client-path", 
    default="./chroma_data", 
    help="Path to the persistent storage for ChromaDB. Default is './chroma_data'."
)
@click.option(
    "--collection-name", 
    default="text", 
    help="Name of the collection to insert data into. Default is 'text'."
)
@click.option(
    "--model-name", 
    default="all-MiniLM-L6-v2", 
    help="Name of the SentenceTransformer model for generating embeddings. Default is 'all-MiniLM-L6-v2'."
)
@click.option(
    "--rebuild/--no-rebuild", 
    default=False, 
    help="Flag to indicate whether to rebuild the collection. Default is False."
)
def add(file_path, client_path, collection_name, model_name, rebuild):
    """Add data to a ChromaDB collection."""
    result = add_data(
        file_path=file_path,
        client_path=client_path,
        collection_name=collection_name,
        model_name=model_name,
        rebuild=rebuild,
    )
    click.echo(f"Data added successfully! {result}")


@cli.command()
@click.option(
    "--query-text", 
    default="dolor amet", 
    help="The text to query against the collection. Default is 'dolor amet'."
)
@click.option(
    "--n-results", 
    default=5, 
    type=int, 
    help="Number of similar results to retrieve. Default is 5."
)
@click.option(
    "--client-path", 
    default="./chroma_data", 
    help="Path to the persistent storage for ChromaDB. Default is './chroma_data'."
)
@click.option(
    "--collection-name", 
    default="text", 
    help="Name of the collection to query. Default is 'text'."
)
@click.option(
    "--model-name", 
    default="all-MiniLM-L6-v2", 
    help="Name of the SentenceTransformer model for generating embeddings. Default is 'all-MiniLM-L6-v2'."
)
def query(query_text, n_results, client_path, collection_name, model_name):
    """Query a ChromaDB collection for similar documents."""
    result = query_collection(
        query_text=query_text,
        n_results=n_results,
        client_path=client_path,
        collection_name=collection_name,
        model_name=model_name,
    )
    click.echo(result)


if __name__ == "__main__":
    cli()
