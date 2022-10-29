// Tutorial for setting up unit tests: https://create-react-app.dev/docs/running-tests/

import { render, screen } from '@testing-library/react';
import App from '../App';
import React from 'react';

test('renders add book button', () => {
  render(<App />);
  const addBookButton = screen.getByText(/Add book/i);
  expect(addBookButton).toBeInTheDocument();
});

it('renders in stock message', () => {
  render(<App />);
  expect(screen.getByText('In Stock')).toBeInTheDocument();
});

it('renders out of stock message', () => {
  render(<App />);
  expect(screen.getByText('Out of Stock')).toBeInTheDocument();
});
