# Example Webapp

Summary description of the webapp goes here...

## Usage of this Template

The Sections below explain the used style guides and configurations for this project.

## Develop

This project uses [React](https://reactjs.org) as the main framework, [eslint](https://eslint.org) for linting, and [prettier](https://prettier.io) for formatting (see [this page](https://prettier.io/docs/en/comparison.html) for learning about linting vs. formatting). The linting rules are listed in [.eslintrc.js](./eslintrc.js). The configuration for prettier can be found in [.prettierrc](./prettierrc). The configurations adhere to [Airbnb's JavaScript style guide](https://github.com/airbnb/javascript).

It was bootstrapped with [Create React App](https://github.com/facebook/create-react-app) (`yarn create react-app react-webapp`) and, thus, uses the pre-configured webpack and babel build tools.

The used package manager for installing packages is [yarn](https://classic.yarnpkg.com/en/docs/install/#mac-stable).

Docs should be written in [jsdoc](https://jsdoc.app/about-getting-started.html) format, though overall we advocate self-explanatory code over comments.

- [ ] TODO: check for JSDOC extension

### Style

When contributing code, please try to make the code following the project's codestyle setup as described in the [Development summary section](./README.md#develop). If you don't have an IDE with installed plugins for eslint or prettier, you can install and run the commands locally (they are added in the [./package.json](./package.json)) like following:

- `./node_modules/.bin/prettier --config .prettierrc --write <path-to-your-modified-file>`
- `./node_modules/.bin/eslint <path-to-your-modified-file>.js`

### Build

#### Production Build

Execute `yarn build` to build the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#### Local Development Build and Run

Execute `yarn start` to run the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### Development Walkthrough

> Add some information here about the structure of the app, what the entrypoint is, and what tools are used.

The project uses follwing structure:

- /src: Contains the source code of the web app, for example the React components. Development usually happens in here. The `/src/index.jsx` is the entry point into the application.
- /public: Contains the default public resources that must be available such as the `index.html`
- /build: The generated directory that contains the bundled web app

- [ ] TODO: add information about the code structure

## More Information about this Template

> Remove this Section from your template for the actual project!

### Installed Packages

Please have a look at the [package.json](https://github.com/mltooling/project-template/blob/react-webapp/react-webapp/package.json) and check whether the dependencies for react, react-scripts etc. should be updated.

### VS Code

- For the settings, have a look at the *Web Development* Section of our [Recommended Settings](https://github.com/mltooling/project-template/blob/main/.vscode/recommended-settings.json).
- For recommended extensions, have a look at the *General Development* and *Web Development* Sections of our [Extensions list](https://github.com/mltooling/project-template/blob/main/.vscode/extensions.json).

### Create React App

#### Available Scripts

In the project directory, you can run:

#### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

#### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

##### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

##### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

##### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

##### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

##### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

##### `yarn build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
