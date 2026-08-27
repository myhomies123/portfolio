---
layout: post
title: About
permalink: /about/
comments: true
---

## Places I Have Lived and Visited

San Diego is home, but I have also spent time in North Carolina and traveled to places including Italy and Hawaii.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }

    .image-gallery figure {
        margin: 0;
        text-align: center;
    }

    .image-gallery figcaption {
        margin-top: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define the data rows for the places in the grid
    const living_in_the_world = [
        {"flag": "https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg", "greeting": "Hi", "description": "San Diego, California - home for about 14 years"},
        {"flag": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Flag_of_North_Carolina.svg", "greeting": "Hi", "description": "North Carolina - lived there for a few months"},
        {"flag": "https://upload.wikimedia.org/wikipedia/en/0/03/Flag_of_Italy.svg", "greeting": "Ciao", "description": "Italy - visited"},
        {"flag": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Flag_of_Hawaii.svg", "greeting": "Aloha", "description": "Hawaii - visited"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = location.flag;
        img.alt = location.description + " flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

My education, activities, and interests have helped shape my path in computer science.

- 🏫 Attended Design39Campus for middle school
- 🎓 Currently attend Del Norte High School
- 🎤 Participate in Speech and Debate
- 🛡️ Build cybersecurity skills through CyberAegis
- 💻 Compete in CyberPatriot and other technology competitions
- 🔐 Interested in cybersecurity and how systems can be protected
- 🧑‍💻 Interested in computer science, programming, and solving technical problems

### Culture, Family, and Fun

Outside of school and technology, I enjoy activities that help me relax, stay active, and spend time with others.

- 🎵 I enjoy listening to music
- 🏅 I like playing and watching sports
- 🍽️ I enjoy trying different foods
- 🐕 I like spending time with my dog
- ✈️ I enjoy traveling and experiencing new places

<comment>
Photo gallery
</comment>
<div class="image-gallery">
  <figure>
    <img src="{{site.baseurl}}/images/about/rohan-travel.jpg" alt="Rohan exploring a city at night">
    <figcaption>Exploring a new city</figcaption>
  </figure>
  <figure>
    <img src="{{site.baseurl}}/images/about/rohan-dog.jpg" alt="Rohan's dog riding in the car">
    <figcaption>My dog</figcaption>
  </figure>
  <figure>
    <img src="{{site.baseurl}}/images/about/california-flag.png" alt="Flag of California">
    <figcaption>California, my home</figcaption>
  </figure>
  <figure>
    <img src="{{site.baseurl}}/images/about/del-norte-foundation.png" alt="Del Norte High School Foundation logo">
    <figcaption>Del Norte High School</figcaption>
  </figure>
</div>
