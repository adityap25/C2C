const data = [
    {
        "ID": 1,
        "Field": "Engineering",
        "Role": "SDE1",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 2,
        "Field": "Engineering",
        "Role": "SDE1",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 3,
        "Field": "Engineering",
        "Role": "FTE",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 4,
        "Field": "Engineering",
        "Role": "Analyst",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 5,
        "Field": "Engineering",
        "Role": "Analyst",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 6,
        "Field": "Engineering",
        "Role": "FTE",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 7,
        "Field": "Engineering",
        "Role": "FTE",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 8,
        "Field": "Engineering",
        "Role": "FTE",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 9,
        "Field": "Engineering",
        "Role": "SDE2",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 10,
        "Field": "Engineering",
        "Role": "Analyst",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 11,
        "Field": "Engineering",
        "Role": "FTE",
        "Experience": 5,
        "Location": "Toronto"
    },
    {
        "ID": 12,
        "Field": "Engineering",
        "Role": "Analyst",
        "Experience": 5,
        "Location": "Toronto"
    }
];

const main = document.getElementById('jobs-display');
const search = document.getElementById('search');
const form = document.getElementById('form');

// showData(data);

function showData(data) {
    main.innerHTML = ``;
    data.forEach(job => {
        const { ID, Field, Role, Experience, Location } = job;
        const job_box = document.createElement('div');
        job_box.classList.add('job');

        job_box.innerHTML = `
            <h3>${Field}</h3>
            <p>${Role}</p>
            <p>Experience :${Experience} years</p>
            <p>Location :${Location}</p>
            <button class="apply-button">Apply/Shortlist</button>
        `
        main.appendChild(job_box);
    })
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const searchTerm = search.value;
    if (searchTerm && searchTerm!="") {
        const datanew = data.filter(function (el) {
            return el.Role.toLowerCase() === searchTerm.toLowerCase()
        }
        );
        showData(datanew);
    }
    else {
        showData(data);
    }
})
