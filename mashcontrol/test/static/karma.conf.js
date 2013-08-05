// Karma configuration
// Generated on Tue Jul 02 2013 14:57:01 GMT+0200 (CEST)


// base path, that will be used to resolve files and exclude
basePath = '../..';


// list of files / patterns to load in the browser
files = [
  JASMINE,
  JASMINE_ADAPTER,
  'static/lib/underscore-1.4.4/underscore-min.js',
  'static/lib/angular-1.0.7/angular.js',
  'static/lib/angular-1.0.7/angular-resource.js',
  'static/lib/angular-1.0.7/angular-mocks.js',
  'static/js/*.js',
  'static/js/**/*.js',
  'test/static/unit/*.js',
  'test/static/unit/**/*.js'
];


// list of files to exclude
exclude = [
  
];


// test results reporter to use
// possible values: 'dots', 'progress', 'junit'
reporters = ['progress'];


// web server port
port = 9876;


// cli runner port
runnerPort = 9100;


// enable / disable colors in the output (reporters and logs)
colors = true;


// level of logging
// possible values: LOG_DISABLE || LOG_ERROR || LOG_WARN || LOG_INFO || LOG_DEBUG
logLevel = LOG_INFO;


// enable / disable watching file and executing tests whenever any file changes
autoWatch = true;


// Start these browsers, currently available:
// - Chrome
// - ChromeCanary
// - Firefox
// - Opera
// - Safari (only Mac)
// - PhantomJS
// - IE (only Windows)
browsers = ['Chrome'];


// If browser does not capture in given timeout [ms], kill it
captureTimeout = 60000;


// Continuous Integration mode
// if true, it capture browsers, run tests and exit
singleRun = false;
