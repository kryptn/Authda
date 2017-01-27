import React from 'react';
import {render} from 'react-dom';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import 'whatwg-fetch';


import {ButtonToolbar} from 'react-bootstrap';
import {ButtonGroup} from 'react-bootstrap';
import {Button} from 'react-bootstrap';
import {Form} from 'react-bootstrap';
import {FormGroup} from 'react-bootstrap';
import {FormControl} from 'react-bootstrap';
import {ControlLabel} from 'react-bootstrap';
import {Grid} from 'react-bootstrap';
import {Row} from 'react-bootstrap';
import {Col} from 'react-bootstrap';

class InviteForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {email: '', referrer: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event){
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({ [name]: value });
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
                      <FormControl name="email"
                        type="email" 
                        placeholder="Email"
                        onChange={this.handleChange}/>
                    </Col>
                  </FormGroup>

                  <FormGroup controlId="formHorizontalReferrer">
                    <Col componentClass={ControlLabel} sm={2}>
                      Referrer
                    </Col>
                    <Col sm={10}>
                      <FormControl
                        name="referrer"
                        type="text" 
                        placeholder="Referrer" 
                        onChange={this.handleChange}/>
                    </Col>
                  </FormGroup>

                  <FormGroup>
                    <Col smOffset={2} sm={10}>
                      <Button type="submit" onClick={this.handleSubmit}>
                        Request an Invite
                      </Button>
                    </Col>
                  </FormGroup>
                </Form>
        )
        return formInstance;
    }
}


class InviteRow extends React.Component {
    constructor(props){
        super(props);
        this.state = props.obj;
    }
    render() {
        const toRender = (
            <Row>
              <Col xs={6} md={4}>{this.state.email}</Col>
              <Col xs={6} md={4}>{this.state.referrer}</Col>
              <Col xs={6} md={4}>
                <ButtonToolbar>
                  <ButtonGroup>
                    <Button name="invite" bsStyle="primary" onClick={this.props.onClick}>Invite</Button>
                    <Button name="reject" bsStyle="danger" onClick={this.props.onClick}>Reject</Button> 
                  </ButtonGroup>
                </ButtonToolbar>
              </Col>
            </Row>
        );
        return toRender;
    }
}


class InviteList extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            invites: [],
        };
    }
    componentDidMount() {
        fetch('/invite/')
        .then(response => response.json())
        .then(json => {
            this.setState({
                invites: json,
            });
        });
    }
    onClick(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name; 

        console.log(name);
        console.log(event);
        //this.setState({ [name]: value });

        /*fetch(this.actionUrl, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ action: action, })
        }).then(
            response => response.json()
        ).then(json => console.log(json));*/
    
    }
    render() {
        const toRender = (
            <Grid>
              {this.state.invites.map(invite => <InviteRow obj={invite} key={invite.id} onClick={this.onClick.bind(this)}/>)}
            </Grid>
        )
        return toRender
    }
}



render(<InviteList/>, document.getElementById('app'));

render(<InviteForm/>, document.getElementById('inviteform'));

