import hyperopt
from hyperopt import fmin, tpe, hp
from hyperopt.mongoexp import MongoTrials
import sys
import task

space = hp.uniform('x', -10, 10)

trials = MongoTrials('mongo://localhost:27017/razlaw/jobs', exp_key=sys.argv[2])


if sys.argv[1] == "search":
	best = fmin(task.objective,
	    space=space,
	    trials=trials,
	    algo=tpe.suggest,
	    max_evals=100)
elif sys.argv[1] == "history":
	hyperopt.plotting.main_plot_history(trials)
elif sys.argv[1] == "histogram":
	hyperopt.plotting.main_plot_histogram(trials)
elif sys.argv[1] == "vars":
	bandit = hyperopt.Bandit(expr=space, do_checks=False)
	hyperopt.plotting.main_plot_vars(trials, bandit=bandit, colorize_best=5)
