import 'package:flutter/material.dart';
import '../models/blog.dart';
import 'blog_detail_screen.dart';

class HomeScreen extends StatelessWidget {
  final List<Blog> blogs = [
    Blog(
      title: 'Flutter Basics',
      author: 'Harun',
      content: 'Flutter is Google’s UI toolkit for building beautiful, natively compiled applications...',
    ),
    Blog(
      title: 'State Management',
      author: 'Rashed',
      content: 'In Flutter, managing state is important. There are many ways like Provider, Riverpod...',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Blog Reader')),
      body: ListView.builder(
        itemCount: blogs.length,
        itemBuilder: (context, index) {
          final blog = blogs[index];
          return ListTile(
            title: Text(blog.title),
            subtitle: Text('By ${blog.author}'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => BlogDetailScreen(blog: blog),
                ),
              );
            },
          );
        },
      ),
    );
  }
}
