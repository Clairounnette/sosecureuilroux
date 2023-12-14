# Website of  SOS écureuils roux et espèces sauvages

Made with [Hugo](https://gohugo.io/) based on Ananke theme.

Most of the content and assets come from http://grifouniou.free.fr/sosecu2/page.2.htm


Welcome to SOS Ecureuil Roux! This Hugo project is dedicated to red squirrel conservation. Whether you are new to web development or just getting started with Hugo, this guide is designed to help you navigate through the project structure and get you up and running.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Hugo](https://gohugo.io/getting-started/installing/)

### Installation

1. Clone this repository to your local machine:

```bash
git clone git@github.com:antscloud/sos_ecureuil_roux.git
```

2. Navigate to the project folder:

```bash
cd sos_ecureuil_roux
```

### Running the Project

To preview the website locally, run the following command:

```bash
hugo server -D
```

This will start a local development server, and you can view the site by opening your browser and going to [http://localhost:1313/](http://localhost:1313/).

## Project Structure

The project is organized as follows:

- **archetypes:** Contains predefined content templates (archetypes) for different sections of your site.
- **content:** Write your content in this directory. Organize it into different sections:
  - **about:** Information about the red squirrel and its conservation efforts.
  - **articles:** Subsections include:
    - corridors: Information about ecological corridors for red squirrels.
    - ecureuils: General content about red squirrels.
    - mangeoires: Details about feeding areas for red squirrels.
    - mineraux: Information on minerals relevant to red squirrels.
    - reservoirs_eau: Water reservoirs and their significance.
    - sauvetage: Content related to rescue efforts for red squirrels.
    - traces: Details about tracking and studying red squirrel traces.
  - **bliobliographie:** Bibliography section listing relevant sources.
  - **contact:** Contact information for SOS Ecureuil Roux.
  - **ecuroducs:** Content related to educational programs about red squirrels.
  - **news:** Subsections include:
    - 2021
    - 2022
    - 2023
- **resources:** Contains generated assets, such as CSS and SCSS files.
- **static:** Add your images and other static files in this directory.
- **themes:** The project uses the "sos" theme, which has its own structure of archetypes, assets, layouts, and partials.

## Writing Content

To add content to your site, navigate to the `content` directory and create or edit markdown files in the respective sections. Add images and other static files to the `static` directory.

## Additional Information

Feel free to explore and customize the theme and content to suit the needs of SOS Ecureuil Roux. If you have any questions, refer to the Hugo documentation or seek assistance from the community.

Happy coding!
