<!-- [![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2sZOX9xt)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<!-- <a name="readme-top"></a> -->
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
 -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> -->


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The Log Viewer is a robust and scalable solution designed to efficiently manage and query large volumes of log data. Traditional logging systems often struggle with performance and scalability issues, especially as the volume of logs grows over time. This project addresses these challenges by incorporating dynamic log sharding, table partitioning, and on-the-fly table creation based on timestamps.

### Key Features

* Table Partitioning: Automatically organizes logs into separate tables based on timestamp, allowing for easy retrieval and management of historical log data.

* Efficient Querying: The system supports effective querying of logs by providing a range of filters such as log level, message content, and timestamp.

* Scalability: The architecture is designed to scale horizontally, accommodating a growing volume of log data without compromising performance.

* User-Friendly API: The API offers a straightforward interface for querying logs, making it accessible for both developers and system administrators.

<!-- Use the `BLANK_README.md` to get started. -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* Flask
* SQLAlchemy
* MySQL
* JavaScript
* HTML
* CSS


<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

* Python 3.12
* Flask
* SQLAlchemy
* MySQL


### Installation

1. Clone the repository
    ```sh
    git clone https://github.com/dyte-submissions/november-2023-hiring-Keshav7802
    ```

2. Install Python dependencies

    ```sh
    cd backend
    pip install -r requirements.txt
    ```

3. Configure the database

    * Create a MySQL database and configure the connection in config.py.
        ```sh
        DB_USERNAME = 'your-username'
        DB_PASSWORD = 'your-password'
        DB_HOST = 'localhost'
        DB_PORT = '3306'
        DB_NAME = 'november_2023_hiring_Keshav7802'
        ```

4. Run the application

    ```sh
    python app.py
    ```
5. For running the WebUI

    ```sh
    cd frontend
    start search.html
    ```
#### You can also use the app_partitioned_tables.py for the partitioned implementation of tables, but overall app.py gives better performance

<!-- _Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- USAGE EXAMPLES -->
## Usage

### Ingesting Logs
We can ingest the logs into Log Viewer using the Post Request, on the port 3000.
For generating the list of logs, we can use **logs_generator.py**
```sh
cd backend
python logs_generator.py
```
After this, we can copy the list of logs from **sample_logs.txt**, and can generate the post request like this with body as the list of logs
```sh
POST/ http://localhost:3000/ingest
```

You can use the curl in **log_ingestion_sample_request.txt** file for better understanding about the Log Ingestion



### Querying Logs Effectively

The Log Viewer provides a robust querying mechanism to filter logs based on multiple criteria. Here's how you can leverage this feature effectively:

#### Filtering by Level
Specify the log level to retrieve logs of a specific severity:

```sh
GET /logs?level=error
```

#### Filtering by Message
Search for logs containing a specific message:

```sh
GET /logs?message=keyword
```

#### Timestamp Range
Retrieve logs within a specific timestamp range:

```sh
GET /logs?timestamp_start=2023-01-01&timestamp_end=2023-02-01
```

#### Combination of Filters
Combine multiple filters for more precise queries:

````sh
GET /logs?level=error&message=keyword&timestamp_start=2023-01-01&timestamp_end=2023-02-01
````
<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- Assumptions Taken -->
## Assumptions Taken

1. In Log ingestion, a post request is made with the list of logs on port 3000 to ingest it into a database.

2. Assumed queries are more frequent, and log ingestion is a one-time process.

3. Field search is based on full text; no partial string searches are required.

4. Assumed there is only one field in the metadata field i.e., parentResourceId

    ```sh
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
    ```

5. Queries are not repeating, i.e., parameters can vary significantly.

<!-- Approach -->
## Approach

1. Since we need to store large volumes of data, one possibility was we store the entire data in NoSQL database because they are
scalable, but since I assumed that queries would be more frequent, I chose to have a SQL database because queries are complex
as involving lots of parameters to check (filtering system).

2. Used indexing for faster querying the database based on different parameters.

3. Also implemented the sharded database version for optimizing the timestamp range queries by storing the logs based on the
year_month of their timestamp. Since, in sharding, we use separate databases and route our requests to them. 
Here, I created different tables for each year_month and queried the tables only which are relevant, hence implementing sharding but specifically 
partitioned tables.

4. But partitioned tables are ineffective for querying based on levels, messages, etc, with an unbounded time range.

5. So, depending on the query type, we can choose the DB logic.


<!-- Future Optimizations -->
## Future Optimizations

1. Since NoSQL databases are known for their scalability, we can use those DBs for storing the entire logs, say for the last 5 to
10 years. But for querying, we can keep some records, say of last one year, in our SQL database. In this way, we can optimize both queries and large-volume storage.

2. We can also use Redis cache (distributed system), which can enhance some efficiency. But that happens only in that case, where we
have repeating queries.

<!-- ROADMAP
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Your Name - [@Keshav Arora](https://www.linkedin.com/in/arora-keshav/) - 78keshav02@gmail.com

Project Link: [https://github.com/dyte-submissions/november-2023-hiring-Keshav7802](https://github.com/dyte-submissions/november-2023-hiring-Keshav7802)

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/image.png
