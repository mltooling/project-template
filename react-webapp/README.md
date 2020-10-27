# Example Webapp

Summary description of the webapp goes here...

## Usage of this Template

The Sections below explain the used style guides and configurations for this project.

## Develop

This project uses [React](https://reactjs.org) as the main framework. Components should be written as [React Hooks](https://reactjs.org/docs/hooks-intro.html) instead of the old class-style wherever possible. Functions should in general be written in the [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) notation. Arrow functions should be defined outside of the `render` function to avoid [any performance problems](https://reactjs.org/docs/faq-functions.html#arrow-function-in-render).

For code styling, [eslint](https://eslint.org) is used for linting and [prettier](https://prettier.io) is used for formatting (see [this page](https://prettier.io/docs/en/comparison.html) for learning about linting vs. formatting). The linting rules are listed in [.eslintrc.js](./eslintrc.js). The configuration for prettier can be found in [.prettierrc](./prettierrc). The configurations adhere to [Airbnb's JavaScript style guide](https://github.com/airbnb/javascript). For CSS styling, [stylelint](https://stylelint.io) is used for which the configuration can be found in the [.stylelintrc.json](./.stylelintrc.json) file.

Docs should be written in [JSDoc](https://jsdoc.app/about-getting-started.html) format, though overall we advocate self-explanatory code over comments.

It was bootstrapped with [Create React App](https://github.com/facebook/create-react-app) (`yarn create react-app react-webapp`) and, thus, uses the pre-configured webpack and babel build tools.

The used package manager for installing packages is [yarn](https://classic.yarnpkg.com/en/docs/install/#mac-stable).

It uses Storybook (see [Section](#storybook)) for documenting components. For more information about testing, check [this Section](#testing).

### Style

When contributing code, please try to make the code following the project's codestyle setup as described in the [Development summary section](#develop). If you don't have an IDE with installed plugins, you can install and run the commands locally (they are added in the [./package.json](./package.json)) like following:

- `./node_modules/.bin/prettier --config .prettierrc --write <path-to-your-modified-file>`: this command formats the file and saves it.
- `./node_modules/.bin/eslint <path-to-your-modified-file>.js`: this command just shows the problems, but does not fix them automatically.
- `./node_modules/.bin/stylelint "**/*.css"`: this commands shows the problems in all your project's css files, but does not fix them automatically.

Sometimes, you have to do something that is not allowed by the linting rules. For example, property spreading in React makes sense sometimes. In this example, you can disable the linter for the specific line by adding `// eslint-disable-line react/jsx-props-no-spreading`. Instead of disabling a rule globally, this forces you to think about your decision instead of allowing slopiness by default.

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

#### Project Structure

The project uses follwing structure:

- `src/`: Contains the source code of the web app, for example the React components. Development usually happens in here. The `/src/index.jsx` is the entry point into the application.
- `public/`: Contains the default public resources that must be available such as the `index.html`
- `build/`: The generated directory that contains the bundled web app. This folder is ignored by `git` and should not be pushed
- `node_modules/`: The installed packages. This folder is ignored by `git` and should not be pushed.

Inside of the `src/` folder, there should be following structure (inspired by this [blog post](https://www.devaradise.com/react-project-folder-structure)):

- `components/`: Capsulated components appear here. Artifacts that are specific to a component should be packaged together, for example `components/dashboard/` should have all components and styles and images that are just relevant for the `dashboard` component.
- `pages/`: Reflects the routes of the application and is composed of different components. Each component in this folder should have its own route.
- `utils/`: Functionality that is generally relevant for your application and could be used in multiple places.
- `app/`: Contains app essentials such as routes and the store in form of `store.js` [when using Redux](https://redux.js.org/tutorials/essentials/part-1-overview-concepts).
- `services/`: Contains JavaScript functions and clients that manage API integrations.
- `assets/`: Should contain style and images and other resources that are generally relevant for your application and not only for a specific component.
- `stories/`: Contains general Storybook files such as introduction and assets that are not directly linked to a specific component. It should not contain the actual component stories.

Add Storybook files (see the [Storybook Section](#storybook)) next to the components they describe. Story files must follow the `<component-name>.stories.jsx` name pattern. For example, if you have a component `src/dashboard/Dashboard.jsx`, put the stories file under `src/dashboard/Dashboard.stories.jsx`.

Add test files next to the code they are testing (see the [Testing Section](#testing)). Test files must follow the `<component-name>.test.jsx` name pattern.

#### Storybook

When we want to document our components further than using JSDoc, we use [Storybook](https://storybook.js.org/docs/react/get-started/introduction). In the [Stories directory](./src/stories/) you can find some example stories (this project was initialized via `npx sb init`).  
The Storybook server can be started via `yarn run storybook`.

#### Testing

This project uses [Jest](https://create-react-app.dev/docs/running-tests) and [react-testing-library](https://github.com/testing-library/react-testing-library) for testing as it comes pre-bundled with _Create React App_.
The official Jest documentation recommends to add at least smoke tests to make sure that components render ([source](https://create-react-app.dev/docs/running-tests#testing-components)), so we go along with this recommendation ;)
Use `test()` instead of it's alias `it()` ([source](https://jestjs.io/docs/en/api.html#testname-fn-timeout)). See the [App.test.jsx](./src/App.test.jsx) file for an example.

To run the tests, execute `yarn test`. To see test coverage, execute `yarn test -- --coverage` ([source](https://create-react-app.dev/docs/running-tests/#coverage-reporting)).

---

## More Information about this Template

> Remove this Section from your template for the actual project!

### Installed Packages

Please have a look at the [package.json](https://github.com/mltooling/project-template/blob/react-webapp/react-webapp/package.json) and check whether the dependencies for react, react-scripts etc. should be updated. Also, check whether package updates influence some configuration files such as the configuration of [.storybook](./.storybook).

### VS Code

- For the settings, have a look at the _Web Development_ Section of our [Recommended Settings](https://github.com/mltooling/project-template/blob/main/.vscode/recommended-settings.json).
- For recommended extensions, have a look at the _General Development_ and _Web Development_ Sections of our [Extensions list](https://github.com/mltooling/project-template/blob/main/.vscode/extensions.json).
- For JSDoc, no extension is needed as it is [built in VS Code](https://code.visualstudio.com/docs/languages/javascript#_jsdoc-support). Just type `\**` and autocomplete. When using types in the comment, VS Code even considers the typing.
- Sometimes, linting errors don't disappear even though you seem to have fixed them. Close the file and re-open it to see whether the error persists.

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
