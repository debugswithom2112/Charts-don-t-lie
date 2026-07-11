let csvData = [];

const Country = document.getElementById("Country");
const Criterion = document.getElementById("Criterion");
const Result = document.getElementById("result");

// Load CSV properly using PapaParse
fetch("/static/2015.csv")
    .then(response => response.text())
    .then(text => {

        const parsed = Papa.parse(text, {
            header: true,
            skipEmptyLines: true
        });

        csvData = parsed.data;

        console.log("CSV Loaded!");
        console.log(csvData);
        console.log("First row:", csvData[0]);
        console.log("Keys:", Object.keys(csvData[0]));

        showValue();

        Country.addEventListener("change", showValue);
        Criterion.addEventListener("change", showValue);
    })
    .catch(err => console.error(err));


function showValue() {

    const selectedCountry = Country.value.trim();
    const selectedCriterion = Criterion.value.trim();

    const row = csvData.find(item =>
        item.Country?.trim() === selectedCountry
    );

    if (!row) {
        Result.textContent = "Country not found.";
        return;
    }

    if (!row[selectedCriterion]) {
        Result.textContent = "Criterion not found.";
        return;
    }

    Result.textContent =
        console.log(`${selectedCountry}'s ${selectedCriterion}: ${row[selectedCriterion]}`);
}