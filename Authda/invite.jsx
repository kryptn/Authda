import React from 'react';
import {render} from 'react-dom';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';

import {Button} from 'react-bootstrap';


class App extends React.Component {
    render () {
        return <p class="text-center"> Hello things <Button> Words!</Button> </p>;
    }
}

render(<App/>, document.getElementById('app'));

