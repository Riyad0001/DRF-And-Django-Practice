import 'package:flutter/material.dart';
import '../models/blog.dart';

class BlogDetailScreen extends StatelessWidget {
  final Blog blog;

  BlogDetailScreen({required this.blog});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(blog.title)),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('By ${blog.author}', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500)),
            SizedBox(height: 20),
            Text(blog.content, style: TextStyle(fontSize: 16)),
          ],
        ),
      ),
    );
  }
}
