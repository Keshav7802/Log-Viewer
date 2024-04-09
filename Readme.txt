Assumptions taken:

1. In Log ingestion, a post request is made with the list of logs on port 3000 to ingest it into a database.
2. Assumed queries are more frequent, and log ingestion is a one-time process.
3. Field search is based on full text; no partial string searches are required.
4. Assumed there is only one field in the metadata field i.e., parentResourceId
{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
5. Queries are not repeating, i.e., parameters can vary significantly.

Approach:

1. Since we need to store large volumes of data, one possibility was we store the entire data in NoSQL database because they are
scalable, but since I assumed that queries would be more frequent, I chose to have a SQL database because queries are complex
as involving lots of parameters to check (filtering system).
2. Used indexing for faster querying the database based on different parameters.
3. Also implemented the sharded database version for optimizing the timestamp range queries by storing the logs based on the
year_month of their timestamp. Since, in sharding, we use separate databases and route our requests to them. Here, I created different
tables for each year_month and queried the tables only which are relevant, hence implementing sharding but specifically 
partitioned tables.
4. But partitioned tables are ineffective for querying based on levels, messages, etc, with an unbounded time range.
5. So, depending on the query type, we can choose the DB logic.

Future Optimizations:

1. Since NoSQL databases are known for their scalability, we can use those DBs for storing the entire logs, say for the last 5 to
10 years. But for querying, we can keep some records, say of last one year, in our SQL database. In this way, we can optimize both queries and large-volume storage.
2. We can also use Redis cache (distributed system), which can enhance some efficiency. But that happens only in that case, where we
have repeating queries.