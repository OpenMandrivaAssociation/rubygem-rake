# Generated from rake-0.9.2.2.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	rake

Summary:	Ruby based make-like utility
Name:		rubygem-%{rbname}

Version:	0.9.2.2
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://rake.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.3.2
BuildArch:	noarch

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies
arespecified in standard Ruby syntax.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/rake
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rake
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/contrib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/contrib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/ext/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/loaders
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/loaders/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGES
%{ruby_gemdir}/gems/%{rbname}-%{version}/MIT-LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/TODO
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes/*.rdoc


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9.2.2-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.2.2-1
+ Revision: 767904
- version update

* Wed Sep 07 2011 Alexander Barakin <abarakin@mandriva.org> 0.9.2-1
+ Revision: 698595
- imported package rubygem-rake

