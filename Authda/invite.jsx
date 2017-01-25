import React from 'react';
import {render} from 'react-dom';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import 'whatwg-fetch';

import {Button} from 'react-bootstrap';

class InviteForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {email: '', referrer: ''};
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(prop, event){

        const state = this.state;
        state[prop] = event.target.value;
        this.setState(state)

    }
    handleSubmit(event){
        const response = fetch('/invite/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: this.state.email,
                referrer: this.state.referrer,
            })
        });

        const data = response.json();
        alert(data);

        
        event.preventDefault();
    }
    render(){
        return (
                <form onSubmit={this.handleSubmit}>
                <label>
                email: <input type="text" value={this.state.email} onChange={this.handleChange.bind(this, 'email')} />
                </label>
                <label>
                referrer: <input type="text" value={this.state.referrer} onChange={this.handleChange.bind(this, 'referrer')} />
                </label>
                <input type="submit" value="Submit" />
                </form>);
    }
}


class App extends React.Component {
    render () {
        return <p className="text-center"> Hello things <Button> Words!</Button> </p>;
    }
}

render(<App/>, document.getElementById('app'));
render(<InviteForm/>, document.getElementById('inviteform'));

