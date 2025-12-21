import argparse


def get_arg_parser(desc: str = 'RL LAB'):
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        '-a',
        '--agent',
        help='agent name {'
                'reinforce, '
                'reinforce_b, '
                'a2c, '
                'dqn, '
                'ddqn, '
                'ppo, '
                '}',
        type=str,
        default='reinforce'
    )
    parser.add_argument(
        '-e',
        '--env',
        help='run type {'
                'CartPole-v1, '
                'LunarLanderContinuous-v2, '
                'Acrobot-v1, '
                'AntBulletEnv-v0}',
        type=str,
        default='CartPole-v1'
    )
    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    agent_name = args.agent
    env_name = args.env
    print(f" >> Agent: {agent_name}, Environment: {env_name}")


if __name__ == "__main__":
    main()
