document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('toggle-explanations').addEventListener('click', function () {
        const concepts = document.querySelectorAll('.concept');
        concepts.forEach(concept => {
            const display = window.getComputedStyle(concept).display;
            if (display === 'none') {
                concept.style.display = 'block';
            } else {
                concept.style.display = 'none';
            }
        });
    });
});

document.getElementById('test-regex').addEventListener('click', function () {
    const regexInput = document.getElementById('regex-input').value;
    const testString = document.getElementById('test-string').value;
    const resultsDiv = document.getElementById('results');

    try {
        const regex = new RegExp(regexInput);
        const matches = testString.match(regex);
        if (matches) {
            resultsDiv.innerHTML = `<p>Matches found: ${matches.length}</p><ul>${matches.map(match => `<li>${match}</li>`).join('')}</ul>`;
        } else {
            resultsDiv.innerHTML = '<p>No matches found.</p>';
        }
    } catch (e) {
        resultsDiv.innerHTML = '<p>Invalid regular expression.</p>';
    }
});


