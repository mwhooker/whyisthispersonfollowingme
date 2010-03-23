<html>
<body>
<h1>intersects</h2>
<h2>FFM (their friends following me)</h2>
<ul>
% for person in c.intersects['FFM']:
    <li>${person['screen_name']}</li>
% endfor
</ul>
<h2>FIF (friends we have in commom, i.e. their friends I follow)</h2>
<ul>
% for person in c.intersects['FIF']:
    <li>${person['screen_name']}</li>
% endfor
</ul>
<h2>FFI (Their followers I follow)</h2>
<ul>
% for person in c.intersects['FFI']:
    <li>${person['screen_name']}</li>
% endfor
</ul>
</body>
</html>
