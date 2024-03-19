/* eslint-disable no-undef */
describe('This is my first Cypress test', () => {
    it('Visits the app and asserts that the title', () => {
        cy.visit('/'); //This works because we assigned the baseURL in our cypress.config file.
        cy.get('h1').should('contain', 'Vite + React');
    })

    it('Checks if clicking button sets count', () => {
        cy.visit('/'); // Visits the site again
        cy.get('button').click() //clicks the button
        cy.get('button').should('contain', '1') //Checks if the button contains 1
    })

    it('Clicks checkbox, checks if ', () => {
        cy.visit('/') //Visits the site again
        cy.get('input').click() //clicks our checkbox input
        cy.get('input').should('be.enabled')
    })

})