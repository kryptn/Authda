import React from 'react';
import {render} from 'react-dom';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import 'whatwg-fetch';


import {Button} from 'react-bootstrap';
import {Form} from 'react-bootstrap';
import {FormGroup} from 'react-bootstrap';
import {FormControl} from 'react-bootstrap';
import {Col} from 'react-bootstrap';

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
        }).then(function(r){
            return r.json()
        });

        const data = response;
        alert(data);

        
        event.preventDefault();
    }
    render(){
        const formInstance = (
                <Form horizontal>
                  <FormGroup controlId="formHorizontalEmail">
                    <Col componentClass={ControlLabel} sm={2}>
                      Email
                    </Col>
                    <Col sm={10}>
                      <FormControl type="email" placeholder="Email" />
                    </Col>
                  </FormGroup>

                  <FormGroup controlId="formHorizontalReferrer">
                    <Col componentClass={ControlLabel} sm={2}>
                      Referrer
                    </Col>
                    <Col sm={10}>
                      <FormControl type="text" placeholder="Referrer" />
                    </Col>
                  </FormGroup>

                  <FormGroup>
                    <Col smOffset={2} sm={10}>
                      <Button type="submit">
                        Request an Invite
                      </Button>
                    </Col>
                  </FormGroup>
                </Form>
        )
        return formInstance;
    }
}


class App extends React.Component {
    render () {

        return <Button  bsStyle="primary" onClick={alert("button!")}>THIS IS A BUTTON</Button>
    }
}

render(<App/>, document.getElementById('app'));
render(<InviteForm/>, document.getElementById('inviteform'));

