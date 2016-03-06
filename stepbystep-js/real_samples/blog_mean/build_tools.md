# Bower

bower manager all the dependency for you by ```bower.json```

## install bower

```sh
npm install bower -g
```

## install packages

```sh
# registered package
bower install <package_name>
# github shorthand
bower install desandro/masonry
# github endpoint
bower install git://git_path
# URl
bower install <url> 
```

## bower.json

```sh
bower init
```

bower.json is generated

```sh
# install and add it to bower.json
bower install <package_name> --save
# install and add it to bower.json with devDependencies
```

## bower configuration

.bowerrc file 

```
{
  "directory": "app/components/",
  "analytics": false,
  "timeout": 120000,
  "registry": {
    "search": [
      "http://localhost:8000",
      "https://bower.herokuapp.com"
    ]
  }
}
```




