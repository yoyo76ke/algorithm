# algorithm


Environment Setup
-----------------

### Git global setup

```
git config --global user.name "Your Name"
git config --global user.email "youremail@**.**"
```

### Prepare

* Choose and open the group fork in your browser.
* Clone group/common repo:

	```
	git clone https://github.com/yoyo76ke/algorithm.git
	```

### Before developing

1. Choose the base branch on group fork

	```
	git checkout master
	```

2. Create a new branch

	```
	git checkout -b {XXX}
	```

### After developing

1. Commit your changes in local repo.

	```
	git add /path/to/files/you/changed
	git commit -m 'XXX the commit message'
	```
 
2. Get updates

	```
	git remote add upstream https://github.com/yoyo76ke/algorithm.git
	git fetch upstream
	git rebase upstream/master
	```
	or

	```
	git remote add upstream https://github.com/yoyo76ke/algorithm.git
	git pull --rebase upstream master
	```
  3. Please resolve the conflicts occured in the step2, then commit your changes.

### Merge changes 

1. Push local commits to GitHub:

	```
	git push origin XXX [--force]
	```

	Note: Need to add `--force` option if fail to push to remote. (**Keep in mind that this will override remote branch with local branch**)
