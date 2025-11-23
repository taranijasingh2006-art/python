# Currency Converter

A simple and efficient currency converter application that allows users to convert between different world currencies using real-time exchange rates.

## Features

- Convert between multiple currencies
- Real-time exchange rate updates
- Support for major world currencies (USD, EUR, GBP, JPY, and more)
- Clean and intuitive user interface
- Responsive design for desktop and mobile.

## Installation

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the root directory and add your API key:
```
API_KEY=your_exchange_rate_api_key
```

4. Start the application:
```bash
npm start
```

## Usage

1. Select the command you want to perform
2. Enter the contry you want to convert from
3. Enter the amount to be converted 
4. Enter the country to which the currency needs to be converted
5. The converted amount will be displayed instantly

## API

This application uses the [ExchangeRate-API](https://www.exchangerate-api.com/) to fetch current exchange rates. You'll need to sign up for a free API key to use this service.

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6+)
- Exchange Rate API

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Exchange rate data provided by ExchangeRate-API
- Icons from Font Awesome
- Inspiration from various currency converter applications

## Contact

For questions or support, please open an issue on GitHub or contact [your-email@example.com](mailto:your-email@example.com).

## Roadmap

- [ ] Add historical exchange rate charts
- [ ] Support for cryptocurrency conversions
- [ ] Offline mode with cached rates
- [ ] Multiple currency conversion at once
- [ ] Currency rate alerts
