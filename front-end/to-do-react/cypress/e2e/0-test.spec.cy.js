/* eslint-disable no-undef */
describe("Tests for", () => {
    it('Visits the app and checks ', () => {
        cy.visit('/'); //visits the main page
        cy.get('ul').children().should("have.length", 15)
    })

    it('Visits the app and deletes both an incomplete and complete task. ', () => {
        cy.visit('/'); //visits the main page
        cy.get('.completed:first > #delete').click()
        cy.get('ul').children().should("have.length", 14)
        cy.get('.notCompleted:first').click().children('#delete').click()
        cy.get('ul').children().should("have.length", 13)
    })

    it('Visits the app and adds a new task', () => {
        cy.visit('');
        cy.get('#textfield').type('test cypress functionality')
        cy.get('#submitButton').click()
        cy.get('ul').children().should("have.length", 16)
    })
})