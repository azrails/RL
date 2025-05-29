# RL
Homeworks of RL course at HSE

<p align="center">
  <a href="#about">About</a> •
  <a href="#installation">Installation</a> •
  <a href="#content">Content</a>
</p>

<div align="center">
  <a href="/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
</div>

## About

This repository contains Python notebooks on Reinforcment Learning (NLP).

## Installation

1. Install [uv](https://docs.astral.sh/uv/#highlights) (dependency management tool):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Install dependencies
```bash
uv sync
```

## Content
<!-- (TEMPLATE)
### 📁 [Project Name](/path/to/directory)
- **Description**: Brief project summary (1-2 sentences)
- **Technologies**: Main technologies/libraries used
- **Key Features**: Core functionality or implemented methods -->

### 📁 [Value/Policy Iteration](./ValuePolicyIteration/ValuePolicyIteration.ipynb)
- **Description**: Solving Markov decision process problem with dynamic programming.
- **Algorithms**: Value Iteration, Policy Iteration

### 📁 [Tabular Learning](TabularLearning/TabularLearning.ipynb)
- **Description**: Experements with tabular learning RL algorithms for Blackjack game.
- **Algorithms**: Q-learning, SARSA, Epected-SARSA

### 📁 [DQN](DDQN/DDQN.ipynb)
- **Description**: Implementation DQN algorithm for solving atari games control.
- **Algorithms**: Dueling Double DQN
- 
- ![Agent](DDQN/videos/game_episode.gif)