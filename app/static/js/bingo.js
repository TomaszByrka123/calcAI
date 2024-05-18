document.querySelectorAll('.bingo-cell').forEach(el => el.addEventListener('click', event => {
    const id = event.target.id;

    if (id === 12) {
        return;
    }

    fetch('/mark-field', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'id': id
        })
    })
        .then(function (response) {

            if (response.ok) {

                response.json()
                    .then(function (response) {
                        console.log(response)
                    });
            } else {
                throw Error('Something went wrong');
            }
        })
        .catch(function (error) {
            console.log(error);
        });

    event.target.classList.add('marked');
}))
