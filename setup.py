from setuptools import setup, find_packages

setup(
    name='tezeta',
    version='0.1',
    packages=find_packages(),
    description='A package for memory in chatbots and LLM requests that uses relevance to maximize context window utilization.',
    author='Rediat Shamsu',
    author_email='rediatbrook@gmail.com',
    url='https://github.com/yourname/tezeta',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='LLM, chatbot, memory, relevance, context window',
    install_requires=[
       'pinecone-client',
       'chromadb',
       'tiktoken'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
)
