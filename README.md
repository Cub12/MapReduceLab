MapReduce Python Simulator

Quickstart
- Create venv and install requirements if needed.
- Run a sample job after scaffolding is complete:
  - python -m src.cli.main run --workers 4 --input data/input --output data/output/wordcount --job student_jobs.word_count.mapper:WordCountMapper,student_jobs.word_count.reducer:WordCountReducer --reducers 4


