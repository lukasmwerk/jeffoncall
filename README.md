# jeffoncall
A grocery recommendation and recipe service that uses user preferences, price/deals data and nutrition knowledge to email you weekly grocery and cooking recommendations to help you save money, save time, and eat your best.

This architecture of this service is rather simple, this is the backend, written using flask.
The frontend dashboard, email service and webscraper live in their own repositories and are deployed seperately.

As the responsibilities of the backend are split in two pretty distinct categories, this repository is layed out as such:
- [API Service](/api_service/README.md): This service implements the backend for dashboards/apps and serves api requests.
- [REC Service](/rec_service/README.md): This service handles actual recommendations, and is spun up periodically to build and send emails.
